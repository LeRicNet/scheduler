class Reservation:

    def set_position(self, position):
        """
        :param position:
        :return: sets position details
        """
        self.position = position

    def position_reset(self):
        """
        :return: zero position
        """
        self._position(0)

    def set_username(self, name):
        self.username = name

    def set_start_date(self, start):
        self.start_date = start

    def set_end_date(self, end):
        self.end_date = end

    def add_notes(self, notes):
        self.notes = notes

if __name__ == '__main__':
    Reservation()
#
# r = Reservation()
# r.set_position(4)
# r.set_username('ep')
# r.set_start_date('1/5/17')
# r.set_end_date('1/8/17')
# r.add_notes("Some notes added")
#
# reservation_list = \
#     {'Position' : r.position,
#      'User' : r.username,
#      'From' : r.start_date,
#      'To' : r.end_date,
#      'Notes' : r.notes}
#
# print(reservation_list)