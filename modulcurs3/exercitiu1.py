
def suma_parametrilor(*args, **kwargs) -> int:
  """
    Returneaza suma parametrilor primiti ca argumente.
  """
  if(args.__len__ == 0):
    return 0
  suma  = 0
  for argumet in args:
    try :
      suma += int(argumet)
    except ValueError:
      pass
  return suma