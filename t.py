import re

def split_sections(sections, max_length=100):
    new_sections = []
    for sec in sections:
        text = sec["text"]
        bold = sec.get("bold", False)
        paragraphs = text.split('\n')
        i = 0
        while i < len(paragraphs):
            para = paragraphs[i].strip()
            if not para:
                new_sections.append({"text": "", "bold": bold})
                i += 1
                continue
            m = re.match(r'^(\d+\.\d+\.?)\s+(.*)', para)
            if m:
                prefix = m.group(1)
                rest = m.group(2)
                sentences = re.split(r'(?<=[.!?]) +', rest)
                buffer = prefix
                for sent in sentences:
                    if not sent.strip():
                        continue
                    if buffer == prefix:
                        buffer += " " + sent
                    elif len(buffer) + len(sent) < max_length:
                        buffer += " " + sent
                    else:
                        new_sections.append({"text": buffer.strip(), "bold": bold})
                        buffer = sent
                if buffer.strip():
                    new_sections.append({"text": buffer.strip(), "bold": bold})
                i += 1
                continue
            sentences = re.split(r'(?<=[.!?]) +', para)
            buffer = ""
            for sent in sentences:
                if not sent.strip():
                    continue
                if len(buffer) + len(sent) < max_length:
                    buffer += (sent + " ")
                else:
                    new_sections.append({"text": buffer.strip(), "bold": bold})
                    buffer = sent + " "
            if buffer.strip():
                new_sections.append({"text": buffer.strip(), "bold": bold})
            i += 1
    return new_sections