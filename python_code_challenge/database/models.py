from python_code_challenge.database import db

class Command(db.Model):
    __tablename__ = 'commands'
    id = db.Column(db.Integer, primary_key=True)
    command_string = db.Column(db.String, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    # store duration of command run time in seconds, rounded to nearest second
    duration = db.Column(db.Integer, nullable=False, default=0)
    output = db.Column(db.BLOB)

    def __init__(self, command_string, length, duration, output):
        self.command_string = command_string
        self.length = length
        self.duration = duration
        self.output = output

    def __repr__(self):
        return "<Command(string='%s', length='%d'), duration='%d', output='%s'>" % (
        self.command_string, self.length, self.duration, self.output)
