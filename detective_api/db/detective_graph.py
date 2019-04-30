from collections import defaultdict
from detective_api.common import logs as logging
from detective_api.common import exceptions as dt_exception

LOG = logging.getLogger(__name__)


class DetectiveGraph:
    def __init__(self):
        # Unique vertex list for wintness events.
        self.witness_event_vertices = []
        # Graph structure for witness events.
        self.witness_event_graph = defaultdict(list)

    @property
    def witness_events(self):
        return self.witness_event_vertices

    @property
    def wt_graph(self):
        return self.witness_event_graph

    def addWinessEentVertices(self, unique_witness_vertices):
        LOG.debug(
            "addWinessEentVertices: initializing unique vertices"
            % (unique_witness_vertices)
        )
        self.witness_event_vertices = unique_witness_vertices

    def addWitnessEventVertex(self, witness_event_name):
        if witness_event_name not in self.witness_event_vertices:
            self.witness_event_vertices.append(witness_event_name)
            self.witness_event_graph[witness_event_name] = []

    def addWitnessEventLink(self, fromEventVetex, toEventVertex=None):
        if fromEventVetex:
            LOG.debug(
                "addWitnessEventLink: adding edge in"
                "graph from Vertex:%s to Vertex:%s "
                % (fromEventVetex, toEventVertex)
            )
            self.witness_event_graph[fromEventVetex].append(toEventVertex)

    def _get_single_path_for_witness_events(
            self, fromeventvertex, toeventvertex, path=[]):
        path = path + [fromeventvertex]
        if fromeventvertex == toeventvertex:
            return path
        if fromeventvertex not in self.witness_event_graph:
            return None
        for linkEventVertex in self.witness_event_graph[fromeventvertex]:
            if linkEventVertex not in path:
                newpath = self._get_single_path_for_witness_events(
                    linkEventVertex,
                    toeventvertex, path
                )
                if newpath:
                    return newpath
        return None

    def _get_all_paths_for_witness_events(
            self, fromeventvertex, toeventvertex, single_path=[]):
        single_path = single_path + [fromeventvertex]

        if fromeventvertex == toeventvertex:
            return [single_path]

        if fromeventvertex not in self.witness_event_graph:
            return []

        multiple_paths = []
        for linkeventvertex in self.witness_event_graph[fromeventvertex]:
            if linkeventvertex not in single_path:
                # Recursively find path destination
                # vertex by exploring all its connected vertex.
                LOG.debug(
                    "_get_all_paths_for_witness_events: "
                    "finding path from Vertex:%s to Vertex:%s "
                    % (linkeventvertex, toeventvertex)
                )
                paths = self._get_all_paths_for_witness_events(
                    linkeventvertex,
                    toeventvertex,
                    single_path
                )
                for path in paths:
                    multiple_paths.append(path)
        return multiple_paths

    def _get_shortest_path_for_witness_events(
            self, fromeventvertex, toeventvertex, single_path=[]):
        single_path = single_path + [fromeventvertex]

        if fromeventvertex == toeventvertex:
            return single_path
        if fromeventvertex not in self.witness_event_graph:
            return None

        shortest = None
        for linkEventVertex in self.witness_event_graph[fromeventvertex]:
            if linkEventVertex not in single_path:
                new_single_path = self._get_shortest_path_for_witness_events(
                    linkEventVertex,
                    toeventvertex,
                    single_path
                )
                if new_single_path:
                    if not shortest or len(new_single_path) < len(shortest):
                        shortest = new_single_path
        return shortest

    def getMultiplePathsForWitnessEvent(self, fromeventvetex, toeventvertex):
        # Get multiple paths for source and destination vertex in the graph.
        # Using DFS way to find path.
        LOG.debug(
            "getMultiplePathsForWitnessEvent: "
            "getting paths from Vertex:%s to Vertex:%s "
            % (fromeventvetex, toeventvertex)
        )
        if fromeventvetex and toeventvertex:
            return self._get_all_paths_for_witness_events(
                fromeventvetex, toeventvertex
            )
        return None

    def _topologicalWitnessEvents(
            self, fromeventvertex, eventverticesvisited, sortedwitnessevents):
        eventverticesvisited[fromeventvertex] = True
        for linkeventvertex in self.witness_event_graph[fromeventvertex]:
            try:
                if not eventverticesvisited[linkeventvertex]:
                    # Recursively sort each conneceted vertices.
                    LOG.debug(
                        "_topologicalWitnessEvents: finding "
                        "topological order path from Vertex:%s "
                        % (linkeventvertex)
                    )
                    self._topologicalWitnessEvents(
                        linkeventvertex,
                        eventverticesvisited,
                        sortedwitnessevents
                    )
            except KeyError:
                raise dt_exception.TopologicalSortKeyError(
                    vertex_key=fromeventvertex
                )

        sortedwitnessevents.insert(0, fromeventvertex)

    def topologicalSortWitnessEvents(self):
        # Topological sorting (DFS) for all witness events
        LOG.debug(
            "topologicalSortWitnessEvents: topological sorting "
            "for vertices %s "
            % self.witness_event_vertices
        )
        eventVerticesVisited = {
            each_vt: False for each_vt in self.witness_event_vertices
        }
        sortedWitnessEventsStack = []

        for eventVertex in self.witness_event_vertices:
            # Find all topological orders for each vertex.
            if not eventVerticesVisited[eventVertex]:
                self._topologicalWitnessEvents(
                    eventVertex,
                    eventVerticesVisited,
                    sortedWitnessEventsStack
                )
        return sortedWitnessEventsStack

    def _check_if_cycle_present(
            self, vertex,
            eventVerticesVisited, eventVerticesStack
    ):

        eventVerticesVisited[vertex] = True
        eventVerticesStack[vertex] = True

        # Recur for all neighbours
        # if any neighbour is visited and in
        for linkeventvertex in self.witness_event_graph[vertex]:
            if not eventVerticesVisited[linkeventvertex]:
                if self._check_if_cycle_present(
                        linkeventvertex,
                        eventVerticesVisited,
                        eventVerticesStack):
                    return True
            elif eventVerticesStack[linkeventvertex]:
                return True

        # Backtracking here..
        eventVerticesStack[vertex] = False
        return False

    def isCyclePresent(self):
        eventVerticesVisited = {
            each_vt: False for each_vt in self.witness_event_vertices
        }
        eventVerticesStack = {
            each_vt: False for each_vt in self.witness_event_vertices
        }

        for each_vertex in self.witness_event_vertices:
            if not eventVerticesVisited[each_vertex]:
                if self._check_if_cycle_present(
                        each_vertex,
                        eventVerticesVisited,
                        eventVerticesStack):
                    return True
        return False
