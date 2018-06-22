def main():
    grid = [["S", "F", "F", "F"], ["F", "H", "F", "H"], ["F", "F", "F", "H"], ["H", "F", "F", "G"]]
    for c in grid:
        row = ""
        for r in c:
            row += r
        print(row
              )
main()