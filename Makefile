
SRCDIR=./src
PROGRAMS=receiver streamer add_rdo
REC_OBJS=$(SRCDIR)/traceline.o $(SRCDIR)/receiver.o
STR_OBJS=$(SRCDIR)/traceline.o $(SRCDIR)/streamer.o
RDO_OBJS=$(SRCDIR)/add_rdo.o
#CFLAGS=-g
CFLAGS=-O2 -Wall 

all: $(PROGRAMS) 

receiver: $(REC_OBJS) 
	$(CC) $(CFLAGS) $(REC_OBJS) -o receiver

streamer: $(STR_OBJS)
	$(CC) $(CFLAGS) $(STR_OBJS) -o streamer 

add_rdo: $(RDO_OBJS)
	$(CC) $(CFLAGS) $(RDO_OBJS) -o add_rdo

receiver.o: $(SRCDIR)/receiver.c $(SRCDIR)/streamer.h
	$(CC) $(CFLAGS) -c $(SRCDIR)/receiver.c
	
streamer.o: $(SRCDIR)/streamer.c $(SRCDIR)/streamer.h
	$(CC) $(CFLAGS) -c $(SRCDIR)/streamer.c

traceline.o: $(SRCDIR)/traceline.c $(SRCDIR)/traceline.h
	$(CC) $(CFLAGS) -c $(SRCDIR)/traceline.c
	
clean:
	rm -f $(PROGRAMS) $(SRCDIR)/*.o


