import csv
import sys
from datetime import datetime


def test_case_01(rows):
    print("01")
    success = False
    for row in rows:
        if (
            str(row["Niveau"]) == "2"
            and row["Allonge"].upper() == "TRUE"
            and row["Assis"].upper() == "TRUE"
        ):
            row["Serie"] = row.get("Serie", 0) + 1
            success = True
        else:
            row["Serie"] = row.get("Serie", 0)
    return success


def test_case_02(rows):
    print("02")
    success = False
    for i, row in enumerate(rows):
        if any(
            r["formattedDate"] == row["formattedDate"] for r in rows if r != row
        ) and any(r["SessionID"] == row["SessionID"] for r in rows if r != row):
            if (
                str(row["Niveau"]) == "2"
                and (row["Allonge"].upper() == "TRUE" or row["Assis"].upper() == "TRUE")
            ) and any(
                str(r["Niveau"]) == "2"
                and (r["Allonge"].upper() == "TRUE" or r["Assis"].upper() == "TRUE")
                for r in rows
                if r != row
            ):
                if i == 1:
                    row["Serie"] = row.get("Serie", 0) + 1
                    success = True
                else:
                    row["Serie"] = row.get("Serie", 0)
            else:
                row["Serie"] = row.get("Serie", 0)
        else:
            print("ERROR")
    return success


def test_case_03(rows):
    print("03")
    success = False
    for i, row in enumerate(rows):
        if any(
            r["formattedDate"] == row["formattedDate"] for r in rows if r != row
        ) and any(r["SessionID"] == row["SessionID"] for r in rows if r != row):
            if (
                str(row["Niveau"]) == "1"
                and row["Allonge"].upper() == "TRUE"
                and row["Assis"].upper() == "TRUE"
            ) and any(
                str(r["Niveau"]) == "1"
                and r["Allonge"].upper() == "TRUE"
                and r["Assis"].upper() == "TRUE"
                for r in rows
                if r != row
            ):
                if i == 1:
                    row["Serie"] = row.get("Serie", 1) + 1
                    success = True
                else:
                    row["Serie"] = row.get("Serie", 0)
            else:
                row["Serie"] = row.get("Serie", 0)
        else:
            print("ERROR")
    return success


def test_case_04(rows):
    print("04")
    count_allonge = 0
    count_assis = 0
    success = False
    for i, row in enumerate(rows):
        if any(
            r["formattedDate"] == row["formattedDate"] for r in rows if r != row
        ) and any(r["SessionID"] == row["SessionID"] for r in rows if r != row):
            if str(row["Niveau"]) == "1" and row["Allonge"].upper() == "TRUE":
                count_allonge += 1
            if str(row["Niveau"]) == "1" and row["Assis"].upper() == "TRUE":
                count_assis += 1
            if count_allonge >= 2 and count_assis >= 2:
                print("Bonjour")
                row["Serie"] = row.get("Serie", 0) + 1
                success = True
            else:
                print("No Count")
                for row in rows:
                    row["Serie"] = row.get("Serie", 0)
        else:
            print("EROR")
    return success


def test_case_05(rows):
    print("05")
    count_allonge = 0
    count_assis = 0
    success = False

    for i, row in enumerate(rows):
        if any(
            r["formattedDate"] == row["formattedDate"] for r in rows if r != row
        ) and any(r["SessionID"] == row["SessionID"] for r in rows if r != row):
            if str(row["Niveau"]) == "1" and row["Allonge"].upper() == "TRUE":
                count_allonge += 1
            if str(row["Niveau"]) == "1" and row["Assis"].upper() == "TRUE":
                count_assis += 1
            if str(row["Niveau"]) == "2" and row["Allonge"].upper() == "TRUE":
                count_allonge += 2
            if str(row["Niveau"]) == "2" and row["Assis"].upper() == "TRUE":
                count_assis += 2
            if count_allonge >= 2 and count_assis >= 2:
                row["Serie"] = row.get("Serie", 0) + 1
                success = True
            else:
                print("No Count")
                for row in rows:
                    row["Serie"] = row.get("Serie", 0)
        else:
            print("Error")
    return success


def test_case_07(rows):
    print("07")
    success = False
    previous_date = None
    series_count = 0
    for i, row in enumerate(rows):
        if any(r["SessionID"] == row["SessionID"] for r in rows if r != row):
            current_date = datetime.strptime(row["formattedDate"], "%d/%m/%Y")
            if previous_date is not None:
                difference = (current_date - previous_date).days
                if difference == 1:
                    row["Serie"] = row.get("Serie", 1)
                    success = True
                else:
                    row["Serie"] = row.get("Serie", 0)
            else:
                series_count += 1
                row["Serie"] = series_count
                success = True

            previous_date = current_date
    return success


def test_case_09(rows):
    print("09")
    success = False
    series_count = 0
    consecutive_days = 0
    lives = 2
    last_date = None

    for row in rows:
        if any(r["SessionID"] == row["SessionID"] for r in rows if r != row):
            current_date = datetime.strptime(row["formattedDate"], "%d/%m/%Y")
            if last_date is None or current_date != last_date:
                if (
                    str(row["Niveau"]) == "2"
                    and row["Allonge"].upper() == "TRUE"
                    and row["Assis"].upper() == "TRUE"
                ):
                    series_count += 1
                    consecutive_days += 1
                    row["Serie"] = series_count
                    success = True
                    if consecutive_days == 5:
                        lives = min(lives + 1, 2)
                        consecutive_days = 0
                else:
                    consecutive_days = 0
                    lives -= 1
                    if lives < 0:
                        series_count = 0
                    row["Serie"] = series_count
                last_date = current_date
            else:
                row["Serie"] = series_count

    return success


def main(input_file):
    with open(input_file, mode="r", encoding="utf-8") as infile, open(
        "output.csv", mode="w", encoding="utf-8", newline=""
    ) as output:
        reader = csv.DictReader(infile)
        fieldNames = reader.fieldnames + ["Serie"]
        writer = csv.DictWriter(output, fieldnames=fieldNames)
        writer.writeheader()
        rows = list(reader)
        if test_case_01(rows):
            if test_case_07(rows):
                if test_case_09(rows):
                    pass
        elif test_case_02(rows):
            pass
        elif test_case_03(rows):
            pass
        elif test_case_04(rows):
            pass
        elif test_case_05(rows):
            pass
        for row in rows:
            writer.writerow(row)


if __name__ == "__main__":
    input_file = sys.argv[1]
    main(input_file)
