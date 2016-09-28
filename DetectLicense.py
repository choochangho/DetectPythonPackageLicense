import json
import pip
import os, sys


package_path = [p for p in sys.path if p.endswith('site-packages')][0]

installed_packages = [package for package in os.listdir(package_path) if package.endswith('dist-info')]

for package in installed_packages:
	meta_file_path = os.path.join(package_path, package, 'metadata.json')

	with open(meta_file_path) as data_file:
		data = json.load(data_file)
		licenses = []
		if "license" in data:
			license = data["license"]
			licenses.append(license)

		if "classifiers" in data:
			classifiers =  [l for l in data["classifiers"] if l.startswith("License")]
			if len(classifiers) > 0:
				for c in classifiers:
					licenses.append(c)

		# Print all package name, version and licenses
		print("%s(%s)" % (data["name"], data["version"]))
		if len(licenses) > 0:
			print("\t%s" % "\n\t".join(licenses))
		else:
			print("\tNot defined")
