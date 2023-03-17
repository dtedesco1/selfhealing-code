def install_libraries():
    try:
        import requests
    except ImportError:
        import os
        os.system("pip install requests")

    try:
        import wikipediaapi
    except ImportError:
        import os
        os.system("pip install wikipedia-api")


def search_attractions(query):
    import wikipediaapi
    wiki_api = wikipediaapi.Wikipedia('en')
    page = wiki_api.page(query)
    return page


def extract_relevant_sections(page):
    sections = [section for section in page.section_by_title('List of').sections]
    return sections


def parse_attractions(sections):
    attractions = []
    for section in sections:
        text = section.text.split('\n')
        for line in text:
            if line:
                title, description = line.split(': ')
                attractions.append((title, description))
                if len(attractions) >= 5:
                    return attractions
    return attractions


def display_results(attractions):
    for attraction in attractions:
        print(f"{attraction[0]}: {attraction[1]}")


def main():
    install_libraries()
    query = "Tourism_in_Paris"
    page = search_attractions(query)
    relevant_sections = extract_relevant_sections(page)
    attractions = parse_attractions(relevant_sections)
    display_results(attractions)


if __name__ == "__main__":
    main()