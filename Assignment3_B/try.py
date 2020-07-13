import csv

file=open('course.csv', 'w')

with file:
  writer = csv.writer(file)
  writer.writerow(["Course Name"])
  writer.writerow(["Web Designing"])
  writer.writerow(["FrontEnd Development"])
  writer.writerow(["Backend Development"])
  writer.writerow(["Database"])
  writer.writerow(["AWS Certification"])
  writer.writerow(["Data Science"])
  writer.writerow(["SEO"])

