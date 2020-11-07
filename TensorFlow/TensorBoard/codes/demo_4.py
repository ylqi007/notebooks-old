import tensorflow as tf
tf.reset_default_graph()   # To clear the defined variables and operations of the previous cell

# create the variables
x_scalar = tf.get_variable('x_scalar', shape=[], initializer=tf.truncated_normal_initializer(mean=0, stddev=1))
x_matrix = tf.get_variable('x_matrix', shape=[30, 40], initializer=tf.truncated_normal_initializer(mean=0, stddev=1))

# ____step 1:____ create the summaries
# A scalar summary for the scalar tensor
scalar_summary = tf.summary.scalar('My_scalar_summary', x_scalar)
# A histogram summary for the non-scalar (i.e. 2D or matrix) tensor
histogram_summary = tf.summary.histogram('My_histogram_summary', x_matrix)

# ____step 2:____ merge all summaries
merged = tf.summary.merge_all()

init = tf.global_variables_initializer()

# launch the graph in a session
with tf.Session() as sess:
    # ____step 3:____ creating the writer inside the session
    writer = tf.summary.FileWriter('./graphs/demo4', sess.graph)
    for step in range(100):
        # loop over several initializations of the variable
        sess.run(init)
        # ____step 4:____ evaluate the merged summaries
        summary = sess.run(merged)
        # ____step 5:____ add summary to the writer (i.e. to the event file) to write on the disc
        writer.add_summary(summary, step)
    print('Done writing the summaries')