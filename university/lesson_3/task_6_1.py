import unittest
import requests
import json


class CreateBook(unittest.TestCase):
    def test_1_create_book(self):

        data_for_book = {
                "title": "ddddet",
                "author": "ooooogfgfgf"

        }

        data_for_update = {
            "author": "update"
        }
        # data_par = {
        #         "name": "Test Name",
        #         "type": "Name for test",
        #         "level": 666,
        #         "book": 1
        # }

        # data_put = {
        #     "name": "Update Name",
        #     "type": "Name for test",
        #     "level": "0",
        #     "book": "1"
        # }


        req = requests.post("http://pulse-rest-testing.herokuapp.com/books/", data=data_for_book)
        self.assertEqual(req.status_code, 201)
        print(type(req))
        idd = req.json()
        print(type(idd))
        self.book_id = req.json()['id']
        # up_get = requests.get("http://pulse-rest-testing.herokuapp.com/books/")
        # print(self.assertIn(self.book_id, up_get.json()))

    def test_2_update(self):
        data_for_update = {
            "author": "update"
        }

        req = requests.put("http://pulse-rest-testing.herokuapp.com/books/" + str(self.book_id), data=data_for_update)
        print(req.status_code)



    def tearDown(self):


        de = requests.delete("http://pulse-rest-testing.herokuapp.com/books/" + str(self.book_id))
        print(de.status_code)

# if __name__ == "__main__":
#     CreateBook.test_1_create_book()




# get_req = requests.get("http://pulse-rest-testing.herokuapp.com/roles")
# print(get_req.status_code)
# print(get_req.text)

# print(json.dumps(get_req.text, indent=4))

#put_req = requests.put("http://pulse-rest-testing.herokuapp.com/roles/121/", data=data_put)
#print(put_req.json())






