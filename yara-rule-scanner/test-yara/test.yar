rule Stuxnet_MadeInPython
{
    meta:
        description = "Rule scanning for tuxnet python source code"
        author = "Jin Kim"
        reference = "https://github.com/kenmueller/stuxnet"
        date = "2020-12-23"
    
    strings:
    // main function include this call stack as a second function call.
        $str1 = "old_infected_attributes = node_infected_attributes(graph)"
    //     def node_total_attributes(graph: nx.Graph) -> dict:
	// filter_for_node_type = lambda node_type: list(filter(lambda node: get_node_type(graph, node) == node_type, graph.node))
	// return {
	// 	NodeType.COMPUTER: len(filter_for_node_type(NodeType.COMPUTER)),
	// 	NodeType.DISCONNECTED_COMPUTER: len(filter_for_node_type(NodeType.DISCONNECTED_COMPUTER)),
	// 	NodeType.USB: len(filter_for_node_type(NodeType.USB)),
	// 	NodeType.PLC: len(filter_for_node_type(NodeType.PLC)),
	// 	'total': len(graph.node)
        $str2 = "NodeType.DISCONNECTED_COMPUTER"

    // found in create-graph.py
    // This line adds router nodes and computer nodes fro all the wireless networks.
    // for router_node in range(NUMBER_OF_LOCAL_WIRED_NETWORKS, NUMBER_OF_LOCAL_NETWORKS):
		// add_computer_nodes(graph, EdgeType.LOCAL_WIRELESS, router_node)
        $str3 = "add_computer_nodes(graph, EdgeType.LOCAL_WIRELESS, router_node)"

        // $str4 = "test"
    
    condition:
        any of them
}