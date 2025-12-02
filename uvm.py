#!/usr/bin/env python3
"""
Модель Учебной Виртуальной Машины
(Пока заглушка, будет расширена в следующих этапах)
"""

class UVM:
    def __init__(self, memory_size=1024):
        self.memory = [0] * memory_size
        self.stack = []
        self.pc = 0
        
    def reset(self):
        """Сброс состояния УВМ"""
        self.memory = [0] * len(self.memory)
        self.stack = []
        self.pc = 0