from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField


class UploadFile(FlaskForm):
    file = FileField()
    submit = SubmitField('Submit Character')


class Character:

    def __init__(self, c_sheet):
        # self.charstat = charstat
        self.c_sheet = c_sheet

    def seeker(self, charstat):
        for row in range(self.c_sheet.nrows):
            for column in range(self.c_sheet.ncols):
                if charstat == self.c_sheet.cell(row, column).value:
                    # if found inside sheet, reads adjacent cel
                    chstatvalue = self.c_sheet.cell(row, column + 1).value
                    return chstatvalue


"""

    def discfilter(self):
        for row in range(self.c_sheet.nrows):
            for column in range(self.c_sheet.ncols):
                if self.charstat == self.c_sheet.cell(row, column).value:
                    if self.c_sheet.cell(row, column + 1).value is not None:
                        chstatvalue = self.charstat
                        return chstatvalue

"""