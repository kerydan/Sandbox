
class DB:
    def __init__(self, con):
        self.con = con

    def set_max_mme_id(self):
        print("DB::set_max_mme_id")

    def get_multi_sign_ids(self):
        ids = []
        ids.append(1);
        ids.extend([3,7])
        return ids

    def SplitMultiSign(self, id, signs):
        root = 900
        s = Sign(root, id + 4);
        signs.append(s);
        s1 = Sign(root, id + 41);
        signs.append(s1);




class Sign:
    root = 0
    id = 0
    id_in_db = 0
    Name = ""
    x, y, width, height = 0 , 0, 0, 0
    sdfs = 9

    def __init__(self, root, id):
        self.root = root
        self.id = id

    def update_view_box(self):
        print('update_view_box')

    def delete_classes(self):
        print('delete_classes')

    def save_to_db(self, db): 
        db.set_max_mme_id()

    def save_to_file(self): 
        print('save to file()')
    


print("Hello w!")
con = 0;
db = DB(con)

multi_sign_ids = db.get_multi_sign_ids()
print(multi_sign_ids)

signs = []

for i in multi_sign_ids:
    db.SplitMultiSign(i, signs);
    print(len(signs), "  ", i, ":")


s = Sign()