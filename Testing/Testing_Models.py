import unittest
from models.model import *
from conn_db.connect_db import *
import interface.home


class Test_Login(unittest.TestCase):
    def setUp(self):
        self.con = DbConnection()
        self.log = Login('bibas', 'password')

    def test_insert(self):
        query = 'insert into users(post_id, position, job_type, language, exp_time, company, username) values(%s, %s, %s, %s, %s, %s, %s);'
        values = (52,'Senior Developer','Part-Time','Python',2,'Freelance Pvt Ltd','bibas')
        self.con.insert(query, values)
        query2 = 'select position, job_type, language, exp_time, company from users where post_id = %s;'
        values = (52,)
        actual = self.con.select_value(query2, values)
        excpt = [('Senior Developer','Part-Time','Python',2,'Freelance Pvt Ltd')]
        self.assertEqual(actual, excpt)


    def test_update(self):
        query = 'update users set position=%s, job_type=%s, language=%s, exp_time=%s, company=%s where post_id = %s;'
        values = ('Junior Web Developer','Full Time','JavaScript',1,'Job pvt ltd',52)
        self.con.update(query, values)
        query2 = 'select position, job_type, language, exp_time, company from users where post_id = %s;'
        values = (52,)
        actual = self.con.select_value(query2, values)
        excpt = [('Junior Web Developer','Full Time','JavaScript',1,'Job pvt ltd')]
        self.assertEqual(actual, excpt)

    def test_get(self):
        self.assertEqual('bibas', self.log.get_username())
        self.assertEqual('password', self.log.get_password())

    def test_set(self):
        self.log.set_password('passwod12')
        self.assertEqual('passwod12', self.log.get_password())

    def tearDown(self):
        self.con = None
        self.log = None


class Test_Register(unittest.TestCase):

    def setUp(self):
        self.reg = Register('ragnar', 'password2', 'password2', 20, 'Itahari', 'Rameshwor Thapa','rameshwor123@gmail.com')

    def test_get(self):
        self.assertEqual('ragnar', self.reg.get_username())
        self.assertEqual('password2', self.reg.get_password())
        self.assertEqual('password2', self.reg.get_password2())
        self.assertEqual(20, self.reg.get_age())
        self.assertEqual('Itahari', self.reg.get_address())
        self.assertEqual('Rameshwor Thapa', self.reg.get_fullname())
        self.assertEqual('rameshwor123@gmail.com', self.reg.get_email())

    def test_set(self):
        self.reg.set_password('password12')
        self.assertEqual('password12', self.reg.get_password())
        self.reg.set_fullname('Sagar Adhikari')
        self.assertEqual('Sagar Adhikari', self.reg.get_fullname())
        self.reg.set_age(22)
        self.assertEqual(22, self.reg.get_age())

    def tearDown(self):
        self.reg = None


class Test_Linear_Search(unittest.TestCase):

    def setUp(self):
        pass

    def test_linear_search(self):
        lst = ['Sahayog', 'Bibas', 'Ram', 'Santosh', 'Pradip', 'Kartik']
        name = 'Bibas'
        self.assertTrue(interface.home.MainPage.linear_search(lst, name))

    def tearDown(self):
        pass


class Test_Bubble_Sort(unittest.TestCase):

    def setUp(self):
        pass

    def test_bubble_sort(self):
        lst = [9, 5, 3, 6, 2, 1, 4, 8, 7]
        actual = (interface.home.MainPage.bubble_sort(lst))
        expect = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(actual, expect)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
