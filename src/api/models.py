from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Tabla User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    direccion_de_entrega = db.Column(db.String(250), unique=False, nullable=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    apellido = db.Column(db.String(120), unique=False, nullable=False)
    celular = db.Column(db.Integer, unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=True)
    favoritos = db.relationship("Favoritos", backref='user' )
    metodosDePagos = db.relationship("MetodosDePagos", backref='user')
    carrito = db.relationship("Carrito", backref='user')

    def __repr__(self):
        return '<User %r' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "is_active": self.is_active,
            "direccion_de_entrega": self.direccion_de_entrega,
            "apellido" : self.apellido,
            "celular": self.celular,


            # do not serialize the password, its a security breach
        }


# Tabla Favoritos
class Favoritos (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    sku = db.Column(db.String(120), db.ForeignKey('producto.sku'), nullable=True )
    


    def __repr__(self):
        return '<Favoritos %r' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "sku": self.sku,
            
        }

#Tabla Metodos de Pago
class MetodosDePagos (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    

    def __repr__(self):
        return '<MetodosDePagos %r' % self.id

    def serialize(self):
        return {
        "id": self.id,
        "id_usuario": self.id_usuario,
        
        }

#Tabla de Carrito
class Carrito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    sku_product = db.Column(db.String(120), db.ForeignKey('producto.sku'),nullable=False )

    def __repr__(self):
        return '<Carrito %r' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "sku_product": self.sku_product,
            
        }
    


#Tabla de Producto
class Producto(db.Model):
    sku = db.Column(db.String(120), primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    productype = db.Column(db.String(120), unique=False, nullable=False)
    product_url = db.Column(db.String(240), unique=True, nullable=False)
    keywords = db.Column(db.String(240), unique=False, nullable=False)
    brand = db.Column(db.String(120), unique=False, nullable=False)
    sell_on_amazon = db.Column(db.Boolean(), unique=False, nullable=False)
    category = db.Column(db.String(120), unique=False, nullable=False)
    price = db.Column(db.Integer, unique=False, nullable=False)
    currency = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.String(500), unique=False, nullable=True)
    rating = db.Column(db.Integer, unique=False, nullable=True)
    main_image =  db.Column(db.String(500), unique=False, nullable=False)
    color = db.Column(db.String(500), unique=False, nullable=True)
    manufacturer = db.Column(db.String(120), unique=False, nullable=True)
    dimensions = db.Column(db.String(120), unique=False, nullable=True)
    carrito = db.relationship("Carrito", backref='producto')
    favoritos = db.relationship("Favoritos", backref='producto')


    def __repr__(self):
        return '<Producto %r' % self.sku

    def serialize(self):
        return {
            "sku": self.sku,
            "name": self.name,
            "productype": self.productype,
            "product_url": self. product_url,
            "keywords": self. keywords,
            "brand": self. brand,
            "sell_on_amazon": self.sell_on_amazon,
            "category": self.category,
            "price": self.price,
            "currency": self.price,
            "description" : self.description,
            "rating": self.rating,
            "main_image": self.main_image,
            "color": self.color,
            "manufacturer": self.manufacturer,
            "dimensions": self.dimensions           
        }
    
    
        

