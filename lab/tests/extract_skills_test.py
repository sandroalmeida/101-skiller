import unittest
from extract_skills import extract_skills

class TestExtractSkills(unittest.TestCase):

    def test_extract_skills(self):
        # Test Case 1
        resume_text = "I have experience in Java, Python, and JavaScript."
        expected_output = ({"Java", "Python", "Javascript"}, set())
        self.assertEqual(extract_skills(resume_text), expected_output)

        # Test Case 2
        resume_text = "I am proficient in Ruby on Rails and ASP.Net."
        expected_output = ({"Ruby", "ASP.Net"}, set())
        self.assertEqual(extract_skills(resume_text), expected_output)

        # Test Case 3
        resume_text = "I have knowledge of HTML, CSS, and Javascript."
        expected_output = ({"HTML", "CSS", "Javascript"}, set())
        self.assertEqual(extract_skills(resume_text), expected_output)

        # Test Case 4
        resume_text = "I am skilled in C++, Rust, and Python."
        expected_output = ({"C++", "Rust", "Python"}, set())
        self.assertEqual(extract_skills(resume_text), expected_output)

        # Test Case 5
        resume_text = "My skills include Powershell, Bash, and Perl."
        expected_output = ({"Powershell", "Bash", "Perl"}, set())
        self.assertEqual(extract_skills(resume_text), expected_output)

        # Test Case 6
        resume_text = "I have expertise in PLSQL, and TSQL."
        expected_output = ({"SQL"}, set())
        self.assertEqual(extract_skills(resume_text), expected_output)

        # Test Case 7
        resume_text = "I am familiar with Objective-C, Golang and Kotlin."
        expected_output = ({"Objective-C", "GoLang", "Kotlin"}, set())
        self.assertEqual(extract_skills(resume_text), expected_output)

        # Test Case 8
        resume_text = "My programming skills include C programming language, Java, and R."
        expected_output = ({"C", "Java"}, set())
        self.assertEqual(extract_skills(resume_text), expected_output)

        # Test Case 9
        resume_text = "I have experience in Java and C#."
        expected_output = ({"Java", "CSharp"}, set())
        self.assertEqual(extract_skills(resume_text), expected_output)

if __name__ == '__main__':
    unittest.main()