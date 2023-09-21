def main():
    score = float(input("Enter score: "))
    result = grade(score)
    print(result)
def grade(score):
  if score < 0:
    return"Invalid score"
  elif score > 100:
    return"Invalid score"
  elif score > 90:
    return"Excellent"
  elif score > 50:
    return"Passable"
  else:
    return"Bad"
if __name__ == "__main__":
    main()