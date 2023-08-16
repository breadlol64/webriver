def search_list(list_to_search: list, search_for, exclude: list = ["a", "an"]):
    results = []
    search_terms = search_for.split(" ")

    for exclude_item in exclude:
        if exclude_item in search_terms:
            search_terms.remove(exclude_item)

    for search_term in search_terms:
        for item in list_to_search:
            if search_term.lower() in item.lower():
                results.append(item)

    return results
