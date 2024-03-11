# Ollama Mistral with Langchain RAG Agent and Custom tools
- Author: Mr.Jack _ www.BICweb.vn
- Start: 03Mar2024
- End: 11Mar2024

## Lý do:
- Một trong những trở ngại cơ bản của người bắt đầu làm AI chatbot đó là phải đăng ký tài khoản, phải trả phí sử dụng ChatGPT cho OpenAI hoặc có model đủ tốt để chạy thử nghiệm. Giờ đây đã có thể chạy được các Model mới nhất (như Llama2, Mistral, Gemma) ngay trên Laptop local (không cần đến cả GPU) với tốc độ rất nhanh nhờ có Ollama và free nhé ^^
- Khi có model đủ tốt để sử dụng, ngay cả với ChatGPT-4 phiên bản mới nhất thì đôi lúc bạn vẫn sẽ chưa hài lòng đơn giản vì ... dữ liệu huấn luyện model bị cũ do chưa kịp cập nhật, hoặc dữ liệu của cá nhân mà ChatGPT không biết được. Vậy phải làm thế nào?
- Bạn muốn em Chatbot "của nhà trồng được" không chỉ biết tiếp chuyện với mình mà còn phải thực hiện được một số nhiệm vụ như hỗ trợ giải quyết công việc thực tế của mình? ... Đó là lúc bạn cần đến ChatAgent với các công cụ mạnh mẽ để hoàn thành công việc ^^
- Khả năng: trò chuyện tán gẫu, tìm kiếm thông tin trên wikipedia (screenshot 1) và đặc biệt là trên arXiv (screenshot 2), chuyên trang công nghệ, giúp những người nghiên cứu các báo cáo công nghệ có trên trang arXiv (https://arxiv.org/archive/cs) một cách nhanh chóng và hiệu quả ^^
- Thời gian vừa qua mình chợt nhận ra việc chia sẻ source code cũng là một động lực mạnh mẽ để thúc đẩy bản thân phải làm mới và tiến bộ mỗi ngày ... Việc người khác đánh giá thế nào không quan trọng bằng việc mình vượt qua được chính mình, vì vậy các bạn hãy thử trải nghiệm và share source code với mọi người nhé 😍🥳

## Nền tảng:
- Cài đặt Ollama và tải xuống các model để chạy local ... thao tác khá nhanh và dễ dàng ^^ - https://ollama.com
- - Download Ollama
  - mở một cửa Terminal để chạy Ollama
  - chạy lệnh 'ollama pull mistral' để download model mistral về máy
  - chạy lệnh 'ollama list' để show các model đã load về máy
  - chạy lệnh 'ollama run mistral' để chạy model mistral vừa tải về
  - mở thêm một cửa sổ Terminal nữa để chạy source code Langchain-RAG-Agent
  - chạy lệnh 'python Advanced_Langchain-RAG_Agent_Custom-Tools_11Mar2024_sendto.py' và thưởng thức em Mistral nổi tiếng trên nền tảng Ollama nhé ^^
- Tìm hiểu thêm về Langchain Agent - https://python.langchain.com/docs/modules/agents/
- và Custom tools cho em nó - https://python.langchain.com/docs/modules/agents/tools/custom_tools
- và Conversation Memory để em nó không bị vấn đề "não cá vàng" ^^ - https://python.langchain.com/docs/modules/memory/

## Screenshot
wikipedia
![alt-text](https://github.com/Mr-Jack-Tung/Ollama-Mistral-with-Langchain-RAG-Agent-and-Custom-tools/blob/main/Ollama%20Mistral%20with%20Langchain%20RAG%20Agent%20and%20Custom%20tools%20-%20Screenshot.jpg)

arXiv
![alt-text](https://github.com/Mr-Jack-Tung/Ollama-Mistral-with-Langchain-RAG-Agent-and-Custom-tools/blob/main/Ollama%20Mistral%20with%20Langchain%20RAG%20Agent%20and%20Custom%20tools%20-%20Screenshot-2.jpg)
