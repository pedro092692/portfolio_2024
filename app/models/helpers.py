from app.extensions import db


def add_item(model, *args):
    new_item = model()
    i = 0

    for column in new_item.__table__.columns:
        if column.name != 'id':
            setattr(new_item, column.name, args[i - 1])
        i += 1

    db.session.add(new_item)
    db.session.commit()

    return new_item


def get_item(model, item_id):
    item = db.get_or_404(model, item_id)
    return item


def update_item(obj_item, *args):
    i = 0
    for column in obj_item.__table__.columns:
        if column.name != 'id' and column.name != 'slug':
            setattr(obj_item, column.name, args[i - 1])
        i += 1
    db.session.commit()


def delete_item(obj_item):
    db.session.delete(obj_item)
    db.session.commit()


def search_item(query, model):
    results = db.paginate(db.select(model).filter(model.name.icontains(query)), per_page=8)
    return results

