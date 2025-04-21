def create_qmsum_gists(pages):
    gists = []
    
    for i, page in enumerate(pages):
        decisions = []
        action_items = []
        key_points = []
        
        lines = [line.strip() for line in page.split('\n') if line.strip()]
        for line in lines:
            lower_line = line.lower()
            
            if any(phrase in lower_line for phrase in ['agree', 'decide', 'conclude', 'resolution']):
                decisions.append(line)
            
            elif any(phrase in lower_line for phrase in ['action', 'task', 'todo', 'assign']):
                action_items.append(line)
              
            elif any(phrase in lower_line for phrase in ['important', 'key point', 'note that']):
                key_points.append(line)
        
        gist_parts = []
        if decisions:
            gist_parts.append(f"Decisions: {decisions[0]}")
        if action_items:
            gist_parts.append(f"Actions: {action_items[0]}")
        if key_points and not (decisions or action_items):  
            gist_parts.append(f"Key Point: {key_points[0]}")
        
        gist = " | ".join(gist_parts) if gist_parts else "Meeting discussion"
        gists.append(f"(Page {i}) {gist}")
    
    return gists
