# Projeto Visão Computacional

## Descrição

Este projeto de visão computacional funciona como uma lousa interativa, consiste em desenhar na tela como o dedo indicador, limpar o desenho com o três dedos e pausar o desenho com 2 dedos. Ele foi desenvolvido utilizando OpenCV, cvzone, mediapipe com o objetivo de desenvolver habilidades de visão computacional e IA.

## Tecnologias Utilizadas

- Python
- OpenCV
- Cvzone
- NumPy
- Mediapipe

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/smfs18/project-computer-vision.git
   cd project-computer-vision
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/macOS
   venv\Scripts\activate  # Para Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como Usar

1. Execute o script principal:
   ```bash
   python main.py
   ```
2. Para testar com uma imagem:
   ```bash
   python main.py --image caminho/para/imagem.jpg
   ```
3. Para testar com um vídeo:
   ```bash
   python main.py --video caminho/para/video.mp4
   ```

## Estrutura do Projeto

```
project-computer-vision/
│-- src/                  # Código-fonte principal
│   │-- main.py           # Script principal
│   │-- utils.py          # Funções auxiliares
│-- requirements.txt      # Dependências do projeto
│-- README.md             # Documentação do projeto
```

## Contribuição

Se deseja contribuir com este projeto, siga os passos abaixo:

1. Faça um fork do repositório
2. Crie uma branch para sua funcionalidade (`git checkout -b minha-feature`)
3. Faça commit das suas alterações (`git commit -m 'Adicionando nova funcionalidade'`)
4. Envie para o repositório remoto (`git push origin minha-feature`)
5. Abra um Pull Request

## Contato

Para mais informações, entre em contato por e-mail: smfs@cin.ufpe.br ou abra uma issue no repositório.
