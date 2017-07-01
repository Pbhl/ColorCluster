import convert_to_csv
import k_means
import cluster_means
import render_image
ip_path = "WIN_20170402_17_26_41_Pro.jpg"
op_path = "output_img.jpg"
convert_to_csv.img_to_csv(ip_path)
k_means.cluster()
cluster_means.calc_mean()
render_image.im_save(op_path)