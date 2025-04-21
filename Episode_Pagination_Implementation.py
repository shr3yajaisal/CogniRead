def paginate_text(text, min_words=200, max_words=400):

    paragraphs = text.split('\n\n')

    pages = []               
    current_page = []        
    current_word_count = 0   

    for para in paragraphs:
        para_word_count = len(para.split())  

        if current_word_count + para_word_count > max_words and current_word_count >= min_words:
            pages.append('\n\n'.join(current_page))
            current_page = [para]
            current_word_count = para_word_count
        else:
            current_page.append(para)
            current_word_count += para_word_count

    if current_page:
        pages.append('\n\n'.join(current_page))
    return pages
