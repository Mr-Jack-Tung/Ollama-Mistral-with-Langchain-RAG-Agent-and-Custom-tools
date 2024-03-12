
# VinAi Translate Vi2En-v2 Model
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer_vi2en = AutoTokenizer.from_pretrained("vinai-translate-vi2en-v2", src_lang="vi_VN")
model_vi2en = AutoModelForSeq2SeqLM.from_pretrained("vinai-translate-vi2en-v2")

tokenizer_en2vi = AutoTokenizer.from_pretrained('vinai-translate-en2vi-v2', src_lang="en_XX")
model_en2vi = AutoModelForSeq2SeqLM.from_pretrained('vinai-translate-en2vi-v2')

def translate_vi2en(vi_text: str) -> str:
    vi_text = vi_text.strip()
    input_ids = tokenizer_vi2en(vi_text, return_tensors="pt").input_ids
    output_ids = model_vi2en.generate(
        input_ids,
        decoder_start_token_id=tokenizer_vi2en.lang_code_to_id["en_XX"],
        num_return_sequences=1,
        num_beams=5,
        early_stopping=True
    )
    en_text = tokenizer_vi2en.batch_decode(output_ids, skip_special_tokens=True)
    en_text = "".join(en_text)
    return en_text.strip()

def translate_en2vi(en_text: str) -> str:
    en_text = en_text.strip()
    input_ids = tokenizer_en2vi(en_text, return_tensors="pt").input_ids
    output_ids = model_en2vi.generate(
        input_ids,
        decoder_start_token_id=tokenizer_en2vi.lang_code_to_id["vi_VN"],
        num_return_sequences=1,
        num_beams=5,
        early_stopping=True
    )
    vi_text = tokenizer_en2vi.batch_decode(output_ids, skip_special_tokens=True)
    vi_text = "".join(vi_text)
    return vi_text.strip()
