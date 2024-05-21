import sec_parser as sp

"""
This module provides functionalities for parsing and extracting specific sections from the Management's Discussion and Analysis (MD&A) of 10-Q filings using the SEC Parser library (`sec_parser`). The main function `parse_management_discussion` uses the parser to extract structured data from a 10-Q document, builds a semantic tree from the elements, and navigates through the tree to identify and extract the MD&A section.

Key functions in the module include:
- `traverse_and_collect_text(node)`: Recursively traverses the semantic tree to collect and concatenate text from all nodes starting from a specified node.
- `traverse_and_collect_types(node)`: Recursively collects the type of each node to help in further processing or filtering of the text data based on semantic meanings assigned during the parsing process.

The `parse_management_discussion(data)` function constructs a semantic tree from the parsed 10-Q data, identifies the 'Management's Discussion and Analysis' section by navigating through titles and subtitles, and extracts relevant text. This script is specifically tailored to parse MD&A sections from SEC filings, providing tools necessary for financial analysis and research.
"""

def traverse_and_collect_text(node):
    texts = [node.text]
    for child in node.children:
        texts.extend(traverse_and_collect_text(child))
    return texts

def traverse_and_collect_types(node):
    types = [node.semantic_element]
    for child in node.children:
        types.extend(traverse_and_collect_types(child))
    return types

def parse_management_discussion(data):
    elements: list = sp.Edgar10QParser().parse(data)

    tree = sp.TreeBuilder().build(elements)

    top_section_title_nodes = []
    nodes = list(tree.nodes)
    for node in nodes:
        if type(node.semantic_element) == sp.semantic_elements.top_section_title.TopSectionTitle:
            top_section_title_nodes.append(node)

    global root
    root = None
    for node in top_section_title_nodes:
        text = "".join(node.text.lower().strip().split()).replace("’", "'")
        if node.parent is not None:
          parent_text = "".join(node.parent.text.lower().strip().split())
          # Part I - Financial Information -> Item 2 - Management's Discussion
          if "financialinformation" in parent_text and "item2" in text:
              root = node

    assert root is not None

    texts = traverse_and_collect_text(root)
    types = traverse_and_collect_types(root)

    include_text=""
    for i in range(len(texts)):
        if type(types[i])==sp.semantic_elements.semantic_elements.TextElement:
            include_text+=f'\n{texts[i]}'
    return include_text