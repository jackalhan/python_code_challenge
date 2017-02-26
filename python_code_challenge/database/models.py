from python_code_challenge.database import db

class Command(db.Model):
    __tablename__ = 'commands'
    id = db.Column(db.Integer, primary_key=True)
    # store file name to identify where the command is located.
    # file name is concatenated with the timestamp.
    file_name = db.Column(db.String, nullable=False)
    command_string = db.Column(db.String, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    # store duration of command run time in seconds, rounded to nearest second
    duration = db.Column(db.Integer, nullable=False, default=0)
    output = db.Column(db.BLOB)

    #unique constraint in order not to store same commands in a particular file.
    __table_args__ = (db.UniqueConstraint('file_name', 'command_string', name='_file_command_unqc'),
                      )
    def __init__(self, file_name, command_string, length, duration, output):
        self.file_name = file_name;
        self.command_string = command_string
        self.length = length
        self.duration = duration
        self.output = output

    def __repr__(self):
        return "<Command (file_name='%s', string='%s', length='%d', duration='%d', output='%s'>" % (
        self.file_name, self.command_string, self.length, self.duration, self.output)

