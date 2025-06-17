import re

def split_sections(sections, max_length=100):
    """Split text sections into smaller chunks based on max_length"""
    new_sections = []
    
    for section in sections:
        text = section["text"]
        bold = section.get("bold", False)
        
        # Handle empty text
        if not text.strip():
            new_sections.append({"text": "", "bold": bold})
            continue
            
        # Split into paragraphs
        paragraphs = text.split('\n')
        
        for paragraph in paragraphs:
            paragraph = paragraph.strip()
            if not paragraph:
                new_sections.append({"text": "", "bold": bold})
                continue
                
            # Check if paragraph starts with numbered item (e.g., "1.2. ")
            numbered_match = re.match(r'^(\d+\.\d+\.?)\s+(.*)', paragraph)
            
            if numbered_match:
                prefix = numbered_match.group(1)
                content = numbered_match.group(2)
                _add_sentences_to_sections(new_sections, content, bold, max_length, prefix)
            else:
                _add_sentences_to_sections(new_sections, paragraph, bold, max_length)
    
    return new_sections

def _add_sentences_to_sections(sections, text, bold, max_length, prefix=""):
    """Helper function to add sentences to sections"""
    sentences = re.split(r'(?<=[.!?]) +', text)
    current_chunk = prefix
    
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
            
        # Add sentence to current chunk
        if current_chunk == prefix:
            current_chunk += " " + sentence if prefix else sentence
        elif len(current_chunk) + len(sentence) + 1 <= max_length:
            current_chunk += " " + sentence
        else:
            # Save current chunk and start new one
            if current_chunk.strip():
                sections.append({"text": current_chunk.strip(), "bold": bold})
            current_chunk = sentence
    
    # Add remaining chunk
    if current_chunk.strip():
        sections.append({"text": current_chunk.strip(), "bold": bold})