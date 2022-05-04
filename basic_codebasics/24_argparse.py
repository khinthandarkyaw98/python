#python3 cmd.py --physics 60 --chemistry 70 --maths 90
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--physics", help = "physics marks")
    parser.add_argument("--chemistry", help = "chemistry marks")
    parser.add_argument("--maths", help = "maths marks")

    args = parser.parse_args()

    phy = int(args.physics)
    chem = int(args.chemistry)
    maths = int(args.maths)
    avg = None

    print(f"--physics {phy} --chemistry {chem} --maths {maths}")

# average
    print(f"the average marks for these three subjects = {(phy + chem + maths)/3}")