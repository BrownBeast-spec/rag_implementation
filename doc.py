def load_data(
        self,
        file: Path,
        max_pages: int =None,
        lan: List[str] =None,
        batch: int =2,
        start:int=None,
        extra_in:Optional[Doct]=None,
    ) -> List[Document]:
#-> List[Document]:indicates that the function will return a list containing Document objects.
#batch_multipler : parameter to control the memory usage and speed of the conversion
#extra_info: dictionary to store additional metadata
#langs : list of languages for OCR, important for processing text in different languages
    from marker.convert import convert_single_pdf
    from marker.models import load_all_models

    model_lst = load_all_models()
    full_text, images, out_meta = convert_single_pdf(
        str(file),
        model_lst,
        max_pages=max_pages,
        langs=langs,
        batch_multiplier=batch_multiplier,
        start_page=start_page,
    )

    doc = Document(text=full_text, extra_info=extra_info or {})

    return [doc]
#format of this 1) load_data from given path, 2)loading models (for ocr and text extraction), 3)then convert the pdf extract the text and store it in structed format like preserving the para's,metadata 4)creating a document object which would include text and data extracted 5) Overall: load model,convert pdf,create doc,return [doc]

