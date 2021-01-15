from .extensions import db

class Project(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   category = db.Column(db.String(20), index=True)
   title = db.Column(db.String(120))
   description = db.Column(db.Text())
   link = db.Column(db.String(120), index=True)
   
   def serialize(self):
      data = {
         'id': self.id,
         'category': self.category,
         'title': self.title,
         'description': self.description,
         'link': self.link
      }

      return data 