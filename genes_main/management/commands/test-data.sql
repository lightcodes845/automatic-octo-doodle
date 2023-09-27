
-- Assembly
INSERT INTO `assembly` (`id`, `accession_id`)
VALUES
	(1,'GCA_000001405.29'),
	(2,'GCA_000001405.14'),
	(3,'GCA_000001635.9');

-- Gene
INSERT INTO `gene` (`gene_id`, `symbol`, `stable_id`)
VALUES
	(1,'JAG1','ENSG00000101384.12'),
	(2,'JAG1','ENSG00000101384.11'),
	(3,'JAG1','ENSG00000101384.7'),
	(4,'JAG1','ENSMUSG00000027276.8'),
	(5,'ACE2','ENSMUSG00000015405.16');


-- Region
INSERT INTO `region` (`region_id`, `name`, `assembly_id`)
VALUES
	(1,'20',1),
	(2,'2',3),
	(3,'X',3),
	(4,'20',2);

-- Transcript
INSERT INTO `transcript` (`transcript_id`, `stable_id`, `gene_id`)
VALUES
	(1,'ENST00000254958.10',1),
	(2,'ENST00000254958.9',2),
	(3,'ENST00000254958.5',3),
	(4,'ENST00000423891.2',3),
	(5,'ENSMUST00000028735.8',4),
	(6,'ENSMUST00000112271.10',5);

-- Transcript Location
INSERT INTO `transcript_location` (`id`, `transcript_id`, `start`, `end`, `region_id`)
VALUES
	(1,1,10637684,10673999,1),
	(2,2,10637684,10674107,1),
	(3,3,10618332,10654694,4),
	(4,4,10618407,10643154,4),
	(5,5,136923376,136958564,2),
	(6,6,162922328,162971416,3);