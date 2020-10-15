import tensorflow as tf
tf.reset_default_graph()   # To clear the defined variables and operations of the previous cell

# create the scalar variable
x_scalar = tf.get_variable('x_scalar', shape=[], initializer=tf.truncated_normal_initializer(mean=0, stddev=1))

# ____step 1:____ create the scalar summary
first_summary = tf.summary.scalar(name='My_first_scalar_summary', tensor=x_scalar)

init = tf.global_variables_initializer()

# launch the graph in a session
with tf.Session() as sess:
    # ____step 2:____ creating the writer inside the session
    writer = tf.summary.FileWriter('./graphs/demo2', sess.graph)
    for step in range(100):
        # loop over several initializations of the variable
        sess.run(init)
        # ____step 3:____ evaluate the scalar summary
        summary = sess.run(first_summary)
        # ____step 4:____ add the summary to the writer (i.e. to the event file)
        writer.add_summary(summary, step)
    print('Done with writing the scalar summary')

