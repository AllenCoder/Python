from MyQR import myqr
import os
version, level, qr_name = myqr.run(
	"12222",
    version=1,
    level='H',
    picture=None,
    colorized=False,
    contrast=1.0,
    brightness=1.0,
    save_name=None,
    save_dir=os.getcwd()
	)