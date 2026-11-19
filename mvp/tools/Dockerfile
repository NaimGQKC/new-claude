FROM python:3.12-slim
RUN pip install --no-cache-dir ddgs==9.16.1 trafilatura==2.3.1 python-docx==1.2.0 openpyxl==3.1.5 python-pptx==1.0.2 reportlab==5.1.0
WORKDIR /app
COPY *.py /app/
EXPOSE 8000
CMD ["python", "server.py"]
