# 🏭 Automação de Esteira Transportadora

Simulação de um sistema de automação industrial em Python, reproduzindo a lógica de um **CLP (Controlador Lógico Programável)** aplicado ao controle de uma esteira transportadora, com sensores e interface de supervisório (HMI).

## 🎯 Objetivo

Demonstrar, de forma prática, como a lógica de automação industrial (normalmente feita em CLPs físicos com linguagem Ladder) pode ser simulada em software, controlando atuadores com base em sinais de sensores.

## ⚙️ Funcionalidades

- Simulação de sensores (presença de peça, fim de curso)
- Lógica de controle de atuadores (motor da esteira, sensores de parada)
- Interface HMI simplificada para acompanhamento do processo
- Testes automatizados da lógica de controle

## 🛠️ Tecnologias

- Python 3

 ## 📁 Estrutura do projeto

automacao-esteira-transportadora/ - pasta src/ com actuators.py, plc_controller.py e hmi.py - pasta tests/ com test_plc_controller.py - README.md

## ▶️ Como executar

python src/plc_controller.py

## 📌 Contexto

Este projeto une minha formação técnica em Automação Industrial com desenvolvimento de software, aplicando conceitos de CLP e supervisório em uma simulação funcional.
