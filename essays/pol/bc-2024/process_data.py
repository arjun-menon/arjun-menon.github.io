#!/usr/bin/env python3

import csv, locale, os

def clean_up():
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    raw_file_name = 'bc-2024-initial-vote-count-oct-21-2024-raw.csv'
    cleaned_up_file_name = 'bc-2024-initial-vote-count-oct-21-2024.csv'
    # I used https://www.convertcsv.com/html-table-to-csv.htm to generate the raw csv from:
    #   https://electionsbcenr.blob.core.windows.net/electionsbcenr/Results_7097_GE-2024-10-19_Party.html
    with open(raw_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')

        cleaned_up = []
        heading_row = next(csv_reader)
        cleaned_up.append([
            heading_row[1],
            heading_row[2],
            heading_row[3],
            heading_row[4],
            heading_row[5],
            heading_row[6],
        ])

        for row in csv_reader:
            cleaned_up.append([
                row[1],
                locale.atoi(row[2]),
                locale.atoi(row[3]),
                locale.atoi(row[4]),
                locale.atoi(row[5]),
                locale.atoi(row[6]),
            ])

        with open(cleaned_up_file_name, 'w', newline='') as clean_csv_file:
            clean_csv_writer = csv.writer(clean_csv_file, delimiter=',')
            for row in cleaned_up:
                clean_csv_writer.writerow(row)

        return cleaned_up

class Riding:
    ridings = [] # call create()
    seat_counts = [0, 0, 0]
    winner_names = {0: 'GP', 1: 'NDP', 2: 'CP'}

    def __init__(self, row):
        self.name = row[0]
        self.relevant_votes = row[1:4]
        self.ndp = row[2]
        self.green = row[1]
        self.progressive_vote = self.ndp + self.green
        self.con = row[3]
        self.other = row[4]
        self.total = row[5]

        self.winner_index = self.relevant_votes.index(max(self.relevant_votes))
        self.seat_counts[self.winner_index] += 1

    def __str__(self):
        return "%s [(NDP: %d + Green: %d) = %d, Con: %d]" % (self.name, self.green, self.ndp, self.progressive_vote, self.con)

    @staticmethod
    def create():
        cleaned_up = clean_up()
        Riding.ridings = [Riding(row) for row in cleaned_up[1:]]

    @staticmethod
    def results():
        print("\nSeat totals:")
        for i in range(0, 3):
            print("%s: %d" % (Riding.winner_names[i], Riding.seat_counts[i]))

    @staticmethod
    def progressiveSplits():
        return [r for r in Riding.ridings if r.winner_index == 2 and r.progressive_vote > r.con]

    @staticmethod
    def printProgressiveSplits():
        print('\nGP+NDP exceeding CP:')
        for r in Riding.progressiveSplits():
            excess = r.progressive_vote - r.con
            print(r, "excess:", excess)


Riding.create()

Riding.results()

Riding.printProgressiveSplits()

