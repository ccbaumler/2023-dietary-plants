def name_scheme():
    if config["db"] == './../Sketched-db/db.crop-plant-entrez.ref.sig.zip':
        return config["group"]+"."+config["k"]+"."+"crop_genome"
    else:
        return config["group"]+"."+config["k"]+"."+"genome"

dir_name = name_scheme()

rule create_directories:
    output:
        directory("output/{dir_name}"),
        directory("output/{dir_name}/sketches"),
        directory("output/{dir_name}/gather"),
        directory("output/{dir_name}/cmon_name_annot")
    shell:
        """
        mkdir -p {output[0]}
        mkdir -p {output[1]}
        mkdir -p {output[2]}
        mkdir -p {output[3]}
        """