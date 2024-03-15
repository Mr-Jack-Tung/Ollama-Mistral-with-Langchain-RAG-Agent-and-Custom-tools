# Ollama Mistral with Langchain RAG Agent and Custom tools
- Author: Mr.Jack _ www.BICweb.vn
- Start: 03Mar2024
- End: 11Mar2024

## Lý do:
- Một trong những trở ngại cơ bản của người bắt đầu làm AI chatbot đó là phải đăng ký tài khoản, phải trả phí sử dụng ChatGPT cho OpenAI hoặc có model đủ tốt để chạy thử nghiệm. Giờ đây đã có thể chạy được các Model mới nhất (như Llama2, Codellama Vicuna, Zephyr, Yi, Phi, Solar, Mistral, Gemma) ngay trên Laptop local (không cần đến cả GPU) với tốc độ rất nhanh nhờ có Ollama, không cần phải đăng ký và đặc biệt là free nhé ^^
- Khi có model đủ tốt để sử dụng, ngay cả với ChatGPT-4 phiên bản mới nhất thì đôi lúc bạn vẫn sẽ chưa hài lòng đơn giản vì ... dữ liệu huấn luyện model bị cũ do chưa kịp cập nhật, hoặc dữ liệu của cá nhân mà ChatGPT không biết được. Vậy phải làm thế nào?
- Bạn muốn em Chatbot "của nhà trồng được" không chỉ biết tiếp chuyện với mình mà còn phải thực hiện được một số nhiệm vụ như hỗ trợ giải quyết công việc thực tế của mình? ... Đó là lúc bạn cần đến ChatAgent với các công cụ mạnh mẽ để hoàn thành công việc ^^
- Khả năng: trò chuyện tán gẫu, tìm kiếm thông tin trên wikipedia (screenshot 1) và đặc biệt là trên arXiv (screenshot 2), chuyên trang công nghệ, giúp những người nghiên cứu các báo cáo công nghệ có trên trang arXiv (https://arxiv.org/archive/cs) một cách nhanh chóng và hiệu quả ^^
- Thời gian vừa qua mình chợt nhận ra việc chia sẻ source code cũng là một động lực mạnh mẽ để thúc đẩy bản thân phải làm mới và tiến bộ mỗi ngày ... Việc người khác đánh giá thế nào không quan trọng bằng việc mình vượt qua được chính mình, vì vậy các bạn hãy thử trải nghiệm và share source code với mọi người nhé 😍🥳

## Nền tảng:
- Cài đặt Ollama và tải xuống các model để chạy local ... thao tác khá nhanh và dễ dàng ^^
  - Download Ollama tại trang web https://ollama.com
  - mở một cửa Terminal để chạy Ollama
  - chạy lệnh 'ollama pull mistral' để download model mistral về máy
  - chạy lệnh 'ollama list' để show các model đã load về máy
  - chạy lệnh 'ollama run mistral' để chạy model mistral vừa tải về
  - mở thêm một cửa sổ Terminal nữa để chạy source code Langchain-RAG-Agent
  - Clone source code và chạy lệnh 'python Advanced_Langchain-RAG_Agent_Custom-Tools_11Mar2024_sendto.py' và thưởng thức em Mistral nổi tiếng trên nền tảng Ollama nhé ^^
- Tìm hiểu thêm về Ollama tại trang github - https://github.com/ollama/ollama
- Tìm hiểu thêm về Langchain Agent - https://python.langchain.com/docs/modules/agents/
- và Custom tools cho em nó - https://python.langchain.com/docs/modules/agents/tools/custom_tools
- và Conversation Memory để em nó không bị vấn đề "não cá vàng" ^^ - https://python.langchain.com/docs/modules/memory/
- Sử dụng thêm VinAI-Translate để mở rộng khả năng làm việc với ngôn ngữ tiếng Việt - https://github.com/VinAIResearch/VinAI_Translate

## Screenshot
#### wikipedia
![alt-text](https://github.com/Mr-Jack-Tung/Ollama-Mistral-with-Langchain-RAG-Agent-and-Custom-tools/blob/main/Ollama%20Mistral%20with%20Langchain%20RAG%20Agent%20and%20Custom%20tools%20-%20Screenshot.jpg)

#### arXiv
![alt-text](https://github.com/Mr-Jack-Tung/Ollama-Mistral-with-Langchain-RAG-Agent-and-Custom-tools/blob/main/Ollama%20Mistral%20with%20Langchain%20RAG%20Agent%20and%20Custom%20tools%20-%20Screenshot-2.jpg)

## Update 12 Mar 2024:
Nếu bạn muốn dùng tiếng Việt kết hợp với Ollama Mistral và Langchain Agent thì có thể bạn sẽ nghĩ kết việc kết hợp VinAI-Translate (https://github.com/VinAIResearch/VinAI_Translate) để dịch câu hỏi tiếng Việt sang tiếng Anh sau đó đưa vào ChatAgent để xử lý trả ra kết quả, rồi lại dùng VinAI-Translate dịch câu trả lời sang tiếng Việt ?! ... mình đã thử và kết quả rất khả quan nhé ^^

![alt-text](https://github.com/Mr-Jack-Tung/Ollama-Mistral-with-Langchain-RAG-Agent-and-Custom-tools/blob/main/VinAI-Translate%20with%20Ollama%20Mistral%20with%20Langchain%20RAG%20Agent%20and%20Custom%20tools%20-%20Screenshot-3.jpg)

## Update 15 Mar 2024:
Mấy hôm vừa rồi mình nghĩ làm sao để chạy được em PhoGPT-4B-Chat trên Ollama thì hay biết mấy, bởi vì muốn chạy em PhoGPT-4B-Chat thì ít nhất cũng phải chạy trên GPU 16BB trở lên. Loay hay tìm kiếm GGUF model PhoGPT-4B-Chat từ sáng đến 1PM thì may quá tìm thấy bạn Tung Nguyen (Data Scientist) có chung sở thích và bạn ấy đã convert xong modle từ MPT sang GGUF rồi ^^ (https://www.linkedin.com/posts/tungxuan0111_error-wrong-number-of-tensors-when-serving-activity-7168256575810289665-nxz0) . Ok, vậy thì tốt rồi, mình vào trang HF của bạn Tung Nguyen (https://huggingface.co/tom1669/PhoGPT-4B-Chat) và download model về và làm theo hướng dẫn trên Youtube ^^ (https://www.youtube.com/watch?v=TFwYvHZV6j0) 

### Gồm những bước sau:
0/ Download PhoGPT-4B-Chat.gguf (7.38 GB) tại trang https://huggingface.co/tom1669/PhoGPT-4B-Chat

1/ Tạo file Modelfile với nội dung:

![alt-text](https://github.com/Mr-Jack-Tung/Ollama-Mistral-with-Langchain-RAG-Agent-and-Custom-tools/blob/main/PhoGPT-4B-Chat-Ollama-Modelfile.jpg)

- FROM "PhoGPT-4B-Chat.gguf"
- TEMPLATE """{{ .System }} ### Câu hỏi: {{ .Prompt }}\n### Trả lời:"""
- PARAMETER stop "\<s\>"
- PARAMETER stop "\<\/s\>"

2/ chạy lệnh 'ollama create PhoGPT-4B-Chat.gguf -f Modelfile'

3/ chạy lệnh 'ollama run PhoGPT-4B-Chat.gguf'

![alt-text](https://github.com/Mr-Jack-Tung/Ollama-Mistral-with-Langchain-RAG-Agent-and-Custom-tools/blob/main/PhoGPT-4B-Chat-Ollama-Setup%26Run.jpg)
