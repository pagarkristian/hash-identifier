HASH_PATTERNS = [
	{
		"name" : "MD5" ,
		"length" : 32 ,
		"regex" : r"^[a-fA-F0-9]{32}$",
		"description" : "Message Digest Algorithm 5 "
} ,

        {
                "name" : "SHA1" ,
                "length" : 40 ,
                "regex" : r"^[a-fA-F0-9]{40}$",
                "description" : "Secure Hash Algorithm 1 "
} ,

        {
                "name" : "SHA224" ,
                "length" : 56 ,
                "regex" : r"^[a-fA-F0-9]{56}$",
                "description" : "Secure Hash Algorithm 224 "
} ,

        {
                "name" : "SHA256" ,
                "length" : 64 ,
                "regex" : r"^[a-fA-F0-9]{64}$",
                "description" : "Secure Hash Algorithm 256 "
} ,

        {
                "name" : "SHA384" ,
                "length" : 96 ,
                "regex" : r"^[a-fA-F0-9]{96}$",
                "description" : "Secure Hash Algorithm 384 "
} ,
        {
                "name" : "SHA512" ,
                "length" : 128 ,
                "regex" : r"^[a-fA-F0-9]{128}$",
                "description" : "Secure Hash Alogrithm 512 "
}

]


PASSWORD_PATTERNS = [

    {
        "name" : "bcrypt" ,
        "regex" : r"^\$2[aby]\$\d{2}\$.{53}$",
        "description" : "bcrypt Password Hash "
} ,

    {
        "name" : "SHA512crypt" ,
        "regex" : r"^\$6\$.*\$[A-Za-z0-9./]{85,86}$",
        "description" : "SHA512crypt Unix Password Hash "
} ,
    {
        "name" : "Argon2" ,
        "regex" : r"^\$argon2(i|d|id)\$.*",
        "description" : "Argon2 Password Hash "
    }
]
