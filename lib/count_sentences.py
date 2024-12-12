#!/usr/bin/env python3
import re

class MyString:
  
  def __init__(self, value="123"):
    self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")
    
  def is_sentence(self):
    return True if self._value[-1] == "." else False
  
  def is_question(self):
    return True if self._value[-1] == "?" else False
  
  def is_exclamation(self):
    return True if self._value[-1] == "!" else False
  
  def count_sentences(self):
    return len(re.findall("[^.?!][.?!]", self._value))

  



