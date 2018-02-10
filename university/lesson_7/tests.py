import unittest



class OurTestCase(unittest.TestCase):
    def test_method_1(self):
        self.assertEqual(4, 7)

    def test_method_2(self):
        self.assertEqual(4, 4)

# test1 = OurTestCase("test_method_1")
# test2 = OurTestCase("test_method_2")
#
# test_suite = unittest.TestSuite([test1, test2])

# test_suite = unittest.TestLoader().loadTestsFromTestCase(OurTestCase)
#
# res = unittest.TestResult()
# print(res)

# test_suite.run(res)
# print(res)

# result = test1.run()
# print(result)

#unittest.main()


if __name__ == "__main__":
    from HtmlTestRunner import HTMLTestRunner
    unittest.main(testRunner=HTMLTestRunner(output=r"/Users/stasy/Downloads/myRepo/university/lesson_3/lesson_7"))


