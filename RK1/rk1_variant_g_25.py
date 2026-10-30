"""РК №1. Монгуш Темир Мергенович, ИУ5-35Б. Вариант Г, 25."""

from operator import itemgetter


class Document:
    """Документ (сторона «один»)."""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Section:
    """Раздел документа (сторона «много»)."""

    def __init__(self, id, name, pages_count, document_id):
        self.id = id
        self.name = name
        self.pages_count = pages_count  # Количественный признак.
        self.document_id = document_id


class SectionDocument:
    """Связь «многие ко многим» между разделами и документами."""

    def __init__(self, document_id, section_id):
        self.document_id = document_id
        self.section_id = section_id


documents = [
    Document(1, "Аналитический отчёт"),
    Document(2, "Архивный регламент"),
    Document(3, "Техническое задание"),
]

sections = [
    Section(1, "Общие положения", 8, 1),
    Section(2, "Анализ данных", 12, 1),
    Section(3, "Порядок хранения", 5, 2),
    Section(4, "Требования к системе", 20, 3),
]

sections_documents = [
    SectionDocument(1, 1),
    SectionDocument(1, 2),
    SectionDocument(2, 3),
    SectionDocument(3, 4),
    SectionDocument(2, 1),  # Раздел 1 входит в два документа.
]


def get_results(documents, sections, sections_documents):
    """Выполнить три запроса варианта Г."""
    # Г1: все документы на кириллическую «А» и их разделы (1:М).
    result_g1 = {
        document.name: [
            section.name
            for section in sections
            if section.document_id == document.id
        ]
        for document in documents
        if document.name.startswith("А")
    }

    # Г2: максимум числа страниц раздела для каждого документа (1:М).
    # Документы без разделов пропускаются: максимум для них не определён.
    result_g2 = []
    for document in documents:
        pages = [
            section.pages_count
            for section in sections
            if section.document_id == document.id
        ]
        if pages:
            result_g2.append((document.name, max(pages)))
    result_g2 = sorted(result_g2, key=itemgetter(1))

    # Г3: соединение через отдельный список связей (М:М).
    many_to_many = [
        (section.name, section.pages_count, document.name)
        for link in sections_documents
        for document in documents
        for section in sections
        if link.document_id == document.id
        and link.section_id == section.id
    ]
    result_g3 = sorted(many_to_many, key=itemgetter(2))
    return result_g1, result_g2, result_g3


def main():
    """Вывести результаты выполнения запросов."""
    result_g1, result_g2, result_g3 = get_results(
        documents, sections, sections_documents
    )
    print("РК №1. Монгуш Темир Мергенович, ИУ5-35Б")
    print("Вариант запросов: Г. Предметная область: 25 (Раздел - Документ)")

    print("\nЗадание Г1 (один ко многим)")
    print("Документы на «А» и список их разделов:")
    for document_name, section_names in result_g1.items():
        print(f"  {document_name}: {', '.join(section_names)}")

    print("\nЗадание Г2 (один ко многим)")
    print("Документы по возрастанию максимального числа страниц раздела:")
    for document_name, max_pages in result_g2:
        print(f"  {document_name}: {max_pages} стр.")

    print("\nЗадание Г3 (многие ко многим)")
    print("Все связанные разделы и документы с сортировкой по документам:")
    for section_name, pages_count, document_name in result_g3:
        print(f"  {document_name} | {section_name} | {pages_count} стр.")


if __name__ == "__main__":
    main()
