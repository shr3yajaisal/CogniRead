def create_quality_gists(pages):
    gists = []
    
    for i, page in enumerate(pages):
        thesis = None
        evidence = []
        conclusions = []
        
        paragraphs = [p.strip() for p in page.split('\n\n') if p.strip()]
        for para in paragraphs:
            first_sentence = para.split('.')[0] + '.'
            
            if not thesis and any(phrase in para.lower() for phrase in 
                               ['this paper', 'we argue', 'hypothesize']):
                thesis = first_sentence[:250]  
                
            elif any(phrase in para.lower() for phrase in 
                    ['study shows', 'data suggest', ' p < ', 'n=']):
                evidence.append(first_sentence)
                
            elif any(phrase in para.lower() for phrase in
                    ['conclusion', 'in summary', 'results indicate']):
                conclusions.append(first_sentence)
        
        gist_parts = []
        if thesis:
            gist_parts.append(f"Thesis: {thesis}")
        if evidence:
            gist_parts.append(f"Evidence: {evidence[0]}")
        if conclusions:
            gist_parts.append(f"Conclusion: {conclusions[-1]}")  # Use last conclusion
        
        gist = " | ".join(gist_parts) if gist_parts else "Academic content"
        gists.append(f"(Page {i}) {gist}")
    
    return gists
