try:
    x=int(input())
   print(x)
except ZeroDivisionError:
    print(ZeroDivisionError)
except ValueError:
    print(ValueError)
except NameError:
    print(NameError)
except IndexError:
    print(IndexError)
except KeyError:
    print(KeyError)
except Exception:
    print(Exception)
except IOError:
    print(IOError)

