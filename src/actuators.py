"""
sensors.py
Simulação de sensores industriais usados no sistema de automação da esteira.

Em um CLP real (Siemens S7-1200), esses sinais viriam de entradas digitais (DI)
conectadas a sensores óticos, indutivos ou de fim de curso. Aqui simulamos o
comportamento físico desses sensores para fins de demonstração e testes.
"""

import random


class Sensor:
    """Classe base para um sensor digital (0/1)."""

    def __init__(self, name: str):
        self.name = name
        self.state = False  # False = 0 (inativo), True = 1 (ativo)

    def read(self) -> bool:
        """Lê o estado atual do sensor (equivalente a ler uma entrada digital do CLP)."""
        return self.state

    def set_state(self, value: bool):
        self.state = value

    def __repr__(self):
        return f"<Sensor {self.name}: {'1' if self.state else '0'}>"


class OpticalSensor(Sensor):
    """
    Sensor óptico de presença — detecta a passagem de uma peça na esteira.
    Usado nos pontos de entrada e saída da esteira transportadora.
    """

    def trigger(self):
        """Simula a passagem de uma peça pelo sensor (pulso de detecção)."""
        self.state = True

    def clear(self):
        self.state = False


class JamSensor(Sensor):
    """
    Sensor de acúmulo/engasgamento — normalmente um sensor óptico posicionado
    após o ponto de entrada. Se uma peça permanecer ativada por tempo além do
    esperado, o CLP interpreta como esteira travada (jam).
    """

    def __init__(self, name: str, jam_probability: float = 0.03):
        super().__init__(name)
        self.jam_probability = jam_probability

    def check_jam(self) -> bool:
        """Probabilidade simulada de ocorrência de um engasgamento em um ciclo de scan."""
        jammed = random.random() < self.jam_probability
        self.state = jammed
        return jammed


class EmergencyStopButton(Sensor):
    """
    Botão de emergência (normalmente fechado — NF). Em um CLP real, a perda de
    sinal (0) indica que o botão foi pressionado, cortando a lógica de segurança.
    """

    def press(self):
        self.state = True

    def release(self):
        self.state = False
