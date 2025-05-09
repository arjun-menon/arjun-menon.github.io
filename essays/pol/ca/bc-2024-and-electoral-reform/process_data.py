#!/usr/bin/env python3

import csv, locale, os

def clean_up():
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    raw_file_name = 'bc-2024-vote-count-csvs/bc-2024-final-vote-count-oct-28-2024-raw.csv'
    cleaned_up_file_name = 'bc-2024-vote-count.csv'
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
    winner_names = {0: 'Green', 1: 'NDP', 2: 'Con'}

    def __init__(self, row):
        self.name = row[0]
        self.green = row[1]
        self.ndp = row[2]
        self.con = row[3]
        self.other = row[4]
        self.total = row[5]
        self.relevant_votes = row[1:5]
        self.progressive_vote = self.ndp + self.green
        self.con_plus = self.con + self.other

        self.progressive_margin = self.progressive_vote - self.con
        self.progressive_margin2 = self.progressive_vote - self.con_plus
        self.hypo_winner = ('Green' if self.green > self.ndp else 'NDP') if self.progressive_vote > self.con_plus else 'Con'

        sorted_votes = list(reversed(sorted(self.relevant_votes)))
        self.winner_index = self.relevant_votes.index(sorted_votes[0])
        self.winner = Riding.winner_names[self.winner_index]
        self.runner_up_index = self.relevant_votes.index(sorted_votes[1])
        self.win_margin = sorted_votes[0] - sorted_votes[1]
        self.seat_counts[self.winner_index] += 1

    def __str__(self):
        return "%s [(NDP: %d + Green: %d) = %d, Con: %d, Oth: %d]" % (self.name, self.ndp, self.green, self.progressive_vote, self.con, self.other)

    @staticmethod
    def create():
        cleaned_up = clean_up()
        Riding.ridings = [Riding(row) for row in cleaned_up[1:]]

        # Progressive splits:
        Riding.progressiveSplits = [r for r in Riding.ridings if r.winner_index == 2 and r.progressive_vote > r.con]
        Riding.progressiveSplits.sort(key=lambda r: r.progressive_margin, reverse=True)

        # Other Vote splits:
        Riding.otherVoteSplits = [r for r in Riding.ridings if (
            r.winner_index in (0,1) and ((r.con + r.other) > r.progressive_vote)
        )]
        Riding.conSplits = [r for r in Riding.otherVoteSplits if r.name != 'Ladysmith-Oceanside']

        # All splits:
        Riding.voteSplits = Riding.progressiveSplits + Riding.conSplits
        Riding.voteSplits.sort(key=lambda r: r.progressive_margin2, reverse=True)

        # Close races:
        Riding.closeRaces = [r for r in Riding.ridings if abs(r.progressive_margin2/r.total) < 0.2]
        Riding.closeRaces.sort(key=lambda r: r.progressive_margin2, reverse=True)

    @staticmethod
    def printResults():
        print("\nSeat totals:")
        for i in range(0, 3):
            print("%s: %d" % (Riding.winner_names[i], Riding.seat_counts[i]))

    @staticmethod
    def printProgressiveSplits():
        print('\nGP+NDP exceeding CP:')
        for r in Riding.progressiveSplits:
            excess = r.progressive_vote - r.con
            print(r, "excess:", excess)

    @staticmethod
    def printOtherVotesSplits():
        print('\nOther vote splits:')
        for r in Riding.otherVoteSplits:
            print(r)


Riding.create()

if __name__ == '__main__':
    for r in Riding.ridings:
        print(r)
    Riding.printResults()
    Riding.printProgressiveSplits()
    Riding.printOtherVotesSplits()

