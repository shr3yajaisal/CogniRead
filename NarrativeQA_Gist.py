def create_narrativeqa_gists(pages):
    gists = []
    
    for i, page in enumerate(pages):
  
        characters = set()
        actions = []
        locations = []
        sentences = [s.strip() for s in page.split('.') if s.strip()]
        for sent in sentences:
            if "'s" in sent or " said" in sent:
                character = sent.split()[0]  
                characters.add(character)
              
            action_verbs = ['went', 'entered', 'opened', 'ran', 'shouted']
            if any(verb in sent for verb in action_verbs):
                actions.append(sent)
            
            location_prepositions = [' in ', ' at ', ' on ', ' near ']
            if any(prep in sent for prep in location_prepositions):
                locations.append(sent.split()[-1])  
        
        gist_parts = []
        if characters:
            gist_parts.append(f"Characters: {', '.join(characters)}")
        if actions:
            gist_parts.append(f"Action: {actions[0]}")
        if locations:
            gist_parts.append(f"Location: {locations[0]}")
        
        gist = ". ".join(gist_parts) if gist_parts else "Story progression"
        gists.append(f"(Page {i}) {gist}")
    
    return gists
