from communities.database import db


class basic_operations():

    def create(self, **kwargs):
        db.session.add(self)
        db.session.commit()
        return self

    def read(self):
        return self.query.get(id=self.id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, **kwargs):
        return self.save(commit)

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self
